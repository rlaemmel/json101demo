# Process JSON dump and produce tag clouds
process: 101wiki.json
	./process.py

# Download JSON dump of 101wiki
101wiki.json:
	curl -k http://data.101companies.org/dumps/Wiki101Full.json > 101wiki.json

# Remove all derived files
clean:
	rm -f 101wiki.json languages.* technologies.*

# git push convenience
push:
	git commit -a
	git push
