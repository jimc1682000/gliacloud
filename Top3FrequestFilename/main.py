urls = [
    "http://www.google.com/a.txt",
    "http://www.google.com.tw/a.txt",
    "http://www.google.com/download/c.jpg",
    "http://www.google.co.jp/a.txt",
    "http://www.google.com/b.txt",
    "https://facebook.com/movie/b.txt",
    "http://yahoo.com/123/000/c.jpg",
    "http://gliacloud.com/haha.png",
]
files=[]
for url in urls :
    segs = url.split("/")
    files.append(segs[-1])

answers={}
fileset=set(files)
for file in fileset :
    answers[file]=files.count(file)
sorted_answers = sorted(answers.items(), key=lambda kv: kv[1], reverse=True)
print(sorted_answers[:3])