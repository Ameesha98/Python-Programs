headline=input("Enter Headline\n")
news=input("Enter news\n")
list=headline.split()
for i in range(len(list)):
    list[i]=list[i].title()
print (' '.join(list))
newsinfo=news.split('. ')
for i in range(len(newsinfo)):
     newsinfo[i]=newsinfo[i].capitalize()
print ('. '.join(newsinfo))

