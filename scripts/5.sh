#/usr/bin/env bash

a=5
hosts=(127.0.0.1 localhost 10.0.2.14)

while (($a \> 0))
do
a=($a-1)
for h in ${hosts[@]}
do
curl $h

if [ `echo $?` == 0 ]
then
echo "Host $h reacheble" >> curl.log
elif [ `echo $?` != 0 ]
then
echo "Host $h unreacheble" >> curl.log
exit										# Добавляем команду оставновки выполения скрипта
fi
done
sleep 1s

done