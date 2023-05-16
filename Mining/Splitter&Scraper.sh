#! /bin/bash

rm -rf GenBankFiles
mkdir GenBankFiles
cd GenBankFiles
awk '/\/\//{n++}{print >"out" n ".txt" }' ../AllGenBank.gb

filelist=$(dir)
touch hosts

for file in $filelist
do
accession=$(grep -w "LOCUS" $file | cut -c 13-24 | xargs)
host=$(grep -w /host $file | grep -o -e '".*"')
echo -e "$accession\t$host">>hosts
mv ./$file ./$accession.gb
done

grep -v '^[[:space:]]*$' hosts | sed 's/"//g' | sort -o hosts
mv hosts ../hosts
