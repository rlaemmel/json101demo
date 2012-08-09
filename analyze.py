#! /usr/bin/env python

import simplejson as json

# Load 101wiki into memory
wiki = json.load(open('101wiki.json', 'r'))

def tagCloud(singular, plural):

    # Determine number of implementations for each key
    tags = dict()
    impls = wiki['Implementation']
    for i in impls:
        impl = impls[i] 
        for k in impl[plural]:
            name = k['name']
            if not name in tags:
                tags[name] = 0
            tags[name] += 1

    # Write frequency map to JSON
    jsonFile = open(plural + '.json', 'w')
    jsonFile.write(json.dumps(tags))

    # Prepare for buckets of scaling
    # Inspired by http://stackoverflow.com/questions/3180779/html-tag-cloud-in-python
    step = max(tags.values()) / 6

    # Apply scaling and write HTML
    htmlFile = open(plural + '.html', 'w')
    htmlFile.write('<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN">\n')
    htmlFile.write('<html>\n')
    htmlFile.write('<head>\n')
    htmlFile.write('  <title>Tag cloud for ' + plural + '</title>\n')
    htmlFile.write('  <link rel="stylesheet" type="text/css" href="style.css"/>\n')
    htmlFile.write('</head>\n')
    htmlFile.write('<body>\n')

    root = 'http://101companies.org/index.php/' + singular
    for tag, count in sorted(tags.items(), key=lambda x: x[1], reverse=True):
        css = count / step        
        htmlFile.write('<a href="%s:%s" class="size-%s">%s</a>\n' % (root, tag, css, tag),)

    htmlFile.write('</body>\n')
    htmlFile.write('</html>\n')
    htmlFile.close()

tagCloud('Language', 'languages')
tagCloud('Technology', 'technologies')
