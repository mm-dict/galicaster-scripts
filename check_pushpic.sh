#!/bin/bash 
SERVICE='run_dashboard_push.py'

CHECK=`ps aux | grep -v grep | grep python | grep -c $SERVICE`

if [ "${CHECK}" == '0' ]
then
    python /usr/share/galicaster/docs/scripts/run_dashboard_push.py &
fi
