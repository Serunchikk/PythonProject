#!/bin/bash

function main {
    echo -e "\nДобро пожаловать в ${USER}"
    date "+%A %d %B %Y, %T"
    memory
    echo
    devices
    echo
}

function memory {
    free -m | awk 'NR==2{printf "Использование памяти: %s/%sMB (%.2f%%)\n", $3,$2,$3*100/$2 }'
    df -h | awk '$NF=="/"{printf "Использование диска: %d/%dGB (%s)\n", $3,$2,$5}'
}

function devices {
    echo "Информация об аппаратуре:"
    sudo hwinfo --short --keyboard
    sudo hwinfo --short --mouse
    sudo hwinfo --short --monitor
    sudo hwinfo --short --gfxcard
    sudo hwinfo --short --sound
    sudo hwinfo --short --storage
}

main
