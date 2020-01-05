from scrapy import cmdline
 
crawl_name = 'googlespider'
paper_list_name = 'paper.txt'
cmd = 'scrapy crawl {0} -a paperlist={1}'.format(crawl_name, paper_list_name)
cmdline.execute(cmd.split())
