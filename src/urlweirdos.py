#!/usr/bin/python3

import sys
import codecs

from pyfaup.faup import Faup

from urlw.plugins import UrlwPlugins
from urlw.log import UrlwLog

def print_help():
    print("\n\t%s url: Run urlweirdos on a single url\n\t%s file: Run urlweirdos against a file\n" % (sys.argv[0], sys.argv[0]))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

    urls_file = None

    try:
        urls_file = codecs.open(sys.argv[1], 'r', 'ascii', errors='ignore')
    except IOError:
        url_arg = sys.argv[1]

    if urls_file is None:
        source_info = "arg:%s" % (sys.argv[1])
    else:
        source_info = "file:%s" % (sys.argv[1])

    urlw_log = UrlwLog(source_info)
    urlw_log.open()
    urlw_log.custom_log("Starting...")
    urlw_p = UrlwPlugins(urlw_log)

    fauplib = Faup()

    if source_info.startswith("arg:"):
        fauplib.decode(sys.argv[1])
        faup_object = fauplib.get()
        for plugin in urlw_p.plugins_list:
            urlw_p.run(plugin, sys.argv[1], faup_object)


#    file_urls=codecs.open(sys.argv[1],'r','ascii',errors='ignore')
#    urls=file_urls.readlines()
#    for url in urls:
#        url=url.replace('\n','')
#        print("URL:[%s]" % (url))
#        f.decode(url, False)
#        print("-----> Extracted TLD:%s" % f.get_tld())
    urlw_log.custom_log("Done")
    urlw_log.close()
