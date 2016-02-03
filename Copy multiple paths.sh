#! /usr/bin/bash
#                                                                                              
# :beginHead                                                                                   
# :author                       :kiran-an                                                       
# :support                      :kiran-an                                                      
# :type                 	:bash                                                                
# :title               		:Faspex data copy                                                          
# :description                  :Copying data from jobs to Faspex upload path                                     
# :endHead                                                                                     
#                                                                                              
# Copyright (C) 2011 The Moving Picture Company              

pathcount=0
wpathcount=0

while read str
do

fname=""
xfile=0

Log_File="$HOME/Desktop/jPatherror_`date '+%d-%m-%Y-%H-%M-%S'`.log"

IFS='/' read -ra ary <<< "$str"
spath=$str

#if [[ "jobs" == ${ary[1]} ]]
if [ -d "$spath" ] || [ -f "$spath" ]
then

	bary=()
	c=0

## Discarding blank element and assiging actual elements to another array

	arysize=$[${#ary[@]}-1]

	for (( c=2; c < ${#ary[@]}; c++ ))
	do
		if [[ $c == $arysize && ${ary[$c]} == *"."* ]] 
		then
			fname=${ary[$c]}
			xfile=1 
			break;
		
		else
			bary[$c]=${ary[$c]}
	
		fi
	done

## Modifying required elements to the actual path

	xsource=()
	x=0
	for key in "${!bary[@]}"
	do 
		xsource[x]=${bary[$key]}	
		x+=1
	done
	

## Creating a folder path

	string=""
	s="/"
	x=""
	for i in ${xsource[@]}
	do
		y=$s$i
		string=$x$y
		x=$string
	done

	dpath="/jobs/tvcResources/bangComms/Faspex/Upload/`date '+%d-%m-%Y'`$string"
	mkdir -p $dpath
	echo ""
	echo "Source path :" $spath
	if [[ $xfile == 1 ]]
	then
		echo ""
		echo " Copying file....."
		`cp -r $spath $dpath`
	else
		echo ""
		echo " Copying directory data to Upload directory.... "
		echo -e "\n"
		`cp -r $spath $dpath`
#		size=`du -sch $path`
	fi

else

	wpathcount=$((wpathcount+1))	
#	Log_File="$HOME/Desktop/jPatherror_`date '+%d-%m-%Y-%H-%M-%S'`.log"
#	echo -e "\n"
#	echo "***Wrong Job paths would be updated in a Log file for you : " $Log_File
#	echo -e "\n"$str | tee -a $Log_File
	echo -e "\n"$str >> $Log_File
fi

done <$HOME/Desktop/jobsfile.txt
echo -e "\n"
echo  $wpathcount ": Wrong paths are updated in a file @ :: "$Log_File
echo -e "\n"
filename="{$HOME/Desktop/Kiran_test.txt}_END"

