for file in $(ls /Users/qingchen/Documents/Data/fmripreptest/testdata); do
	echo "${file: 4: 8}";
	sh fmriprep.sh ${file: 4: 8}
done