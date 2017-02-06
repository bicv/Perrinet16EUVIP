default: html

SRC=2016-10-26_Perrinet16EUVIP_talk

edit:
	atom $(SRC).py

html:
	python3 $(SRC).py
	open -a safari $(SRC).html

blog:
	python3 $(SRC).py
	rsync -av $(SRC).html ~/pool/blog/invibe/files/
	cd ~/pool/blog/invibe/ ; nikola build
	cd ~/pool/blog/invibe/ ; nikola deploy
	open http://blog.invibe.net/files/$(SRC).html

