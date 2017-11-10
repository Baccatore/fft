while read filename
do
	python3 ./fft.py "${filename}"
done < filelist.txt
