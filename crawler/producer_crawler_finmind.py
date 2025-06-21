from crawler.tasks_crawler_finmind import crawler_finmind

# for 迴圈, 可一次發送多個任務
for data_dir in ["2330", "0050", "2317", "0056", "00713"]:
    print(data_dir)
    crawler_finmind.delay(data_dir=data_dir)
