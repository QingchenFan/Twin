echo $1

docker run --rm -v /Users/qingchen/Documents/Data/fmripreptest/wd:/wd \
-v /Users/qingchen/Documents/Data/fmripreptest/testdata/:/input \
-v /Users/qingchen/Documents/Data/fmripreptest/fmriprepout/derivatives:/out \
-v /Users/qingchen/Documents/Data/freesurferlicense/:/freesurfer_license \
nipreps/fmriprep:23.0.2 /input /out participant \
-w /wd \
--participant_label $1 \
--output-spaces T1w MNI152NLin6Asym:res-2 MNI152NLin2009cAsym:res-2 \
--fs-license-file /freesurfer_license/license.txt \
--cifti 91k \
--skip-bids-validation \
