#!/bin/bash
# Batch Folder Add
# Written By: Carmen Atkins
# July 28, 2021
# This script creates 25 blank folders
#..............................................................................
# Collecting User(Folder) Name
#.............................................................................
echo "Hello, please type your name."
read NAME
echo "Thank you $NAME. I will create your directories now."
#.............................................................................
#Counting number of existing Folders
#............................................................................
COUNT=$(ls | grep $NAME | cut -d '-' -f 2 | sort -nr | head -n1)
if [ -z "$COUNT" ]
then  echo "\$COUNT was NULL. Starting file count at 0."
INITIALCOUNT=0
#............................................................................
#Creating 25 new folders starting at 0
#...........................................................................
FINALCOUNT=$(($INITIALCOUNT+25))
while [ $INITIALCOUNT -lt $FINALCOUNT ]
do
        touch $NAME-$INITIALCOUNT
        ((INITIALCOUNT++))
done
echo "25 folders named $NAME have been created."

else
 echo "\$COUNT was NOT NULL. Starting file count at $COUNT"
INITIALCOUNT=$(($COUNT+1))
#............................................................................
#Creating 25 new folders based on number of initial folders
#...........................................................................
FINALCOUNT=$(($INITIALCOUNT+25))
while [ $INITIALCOUNT -lt $FINALCOUNT ]
do
        touch $NAME-$INITIALCOUNT
        ((INITIALCOUNT++))
done

echo "25 folders named $NAME have been created."

fi

exit
