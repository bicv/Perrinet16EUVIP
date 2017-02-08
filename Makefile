default: html

html:
	#cd docs; python3 2016-10-26_Perrinet16EUVIP_talk.py
	cd docs; jupyter nbconvert --to=html ../notebooks/EUVIP_0.ipynb --output=../docs/index.html
	cd docs; jupyter nbconvert --to=html ../notebooks/EUVIP_1_defaults.ipynb --output=../docs/EUVIP_1_defaults.html
	cd docs; jupyter nbconvert --to=html ../notebooks/EUVIP_2_lena.ipynb --output=../docs/EUVIP_2_lena.html
	cd docs; jupyter nbconvert --to=html ../notebooks/EUVIP_3-sparsecoding.ipynb --output=../docs/EUVIP_3-sparsecoding.html
	cd docs; jupyter nbconvert --to=html ../notebooks/EUVIP_4-statistics_natural_images.ipynb --output=../docs/EUVIP_4-statistics_natural_images.html
	cd docs; jupyter nbconvert --to=html ../notebooks/EUVIP_5-activities-fits.ipynb --output=../docs/EUVIP_5-activities-fits.html
	cd docs; jupyter nbconvert --to=html ../notebooks/EUVIP_6-droplets.ipynb --output=../docs/EUVIP_6-droplets.html
