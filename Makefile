default: html

html:
	#cd docs; python3 2016-10-26_Perrinet16EUVIP_talk.py
	cd docs; jupyter nbconvert --to=html ../notebooks/EUVIP_0.ipynb index.html
