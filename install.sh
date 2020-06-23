#!/usr/bin/env bash

if [[ $EUID -ne 0 ]]; then
	echo "This script must be run as root."
	exit 1
fi

case "$(uname -s)" in
	Linux)
		if [[ ! -z "$(which apt 2>/dev/null)" ]]; then
			install="sudo apt install -y"
			commands=$(cat<<-EOT
				sudo apt update -y && sudo apt upgrade -y
				sudo apt install python -y
			EOT
			)
		elif [[ ! -z "$(which pacman 2>/dev/null)" ]]; then
			install="sudo pacman -S --noconfirm"
			commands=$(cat<<-EOT
				sudo pacman -Syu --noconfirm
				sudo pacman -S python --noconfirm
			EOT
			)
		else
			echo "Can't find package manager."
			exit 1
		fi

		echo "Select python package installer."
		options=("PIP" "Easy Install")
		select option in "${options[@]}"
		do
			case $option in
				"PIP")
					commands=$(cat<<-EOT
						$commands
						$install python-pip
						pip install -r requirements.txt
					EOT
					)
					break
					;;
				"Easy Install")
					commands=$(cat<<-EOT
						$commands
						$install python-setuptools
						sudo easy_install \$(cat requirements.txt)
					EOT
					)
					break
					;;
			esac
		done

		echo "Select browser for the bot."
		options=("Google Chrome" "Mozilla Firefox")
		select option in "${options[@]}"
		do
			case $option in
				"Google Chrome")
					commands=$(cat<<-EOT
						$commands
						$install chromium
					EOT
					)
					break
					;;
				"Mozilla Firefox")
					if [[ "$(uname -m)" == "x86_64" ]]; then
						arch=32
					else
						arch=64
					fi
					commands=$(cat<<-EOT
						$commands
						wget "https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux$arch.tar.gz"
						tar -xvzf geckodriver*
						sudo chmod +x geckodriver
						sudo mv geckodriver /usr/bin
						sudo rm geckodriver*
					EOT
					)
					break
					;;
			esac
		done
		;;
	Darwin)
		commands=$(cat<<-EOT
			brew update && brew upgrade
			brew install python
			pip install -r requirements.txt
		EOT
		)
		echo "Select browser for the bot."
		options=("Google Chrome" "Mozilla Firefox")
		select option in "${options[@]}"
		do
			case $option in
				"Google Chrome")
					commands=$(cat<<-EOT
						$commands
						brew install chromium
					EOT
					)
					break
					;;
				"Mozilla Firefox")
					commands=$(cat<<-EOT
						$commands
						wget "https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-macos.tar.gz"
						tar -xvzf geckodriver*
						sudo chmod +x geckodriver
						sudo mv geckodriver /usr/bin
						sudo rm geckodriver*
					EOT
					)
					break
					;;
			esac
		done
		;;
	*)
		echo "Your OS is not supported."
		exit 1
		;;
esac
eval "${commands}"