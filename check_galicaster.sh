#!/bin/bash 
SERVICE='galicaster'

CHECK=`ps aux | grep -v grep | grep python | grep -c $SERVICE`

if [ "${CHECK}" == '0' ]
then
    nohup /usr/bin/galicaster &
    uname -a | mail -s "$SERVICE down" icto
fi
