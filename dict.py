def csdict(cs):
    d={}
    for i in cs.split(";"):
          k,v=i.split("=")
          d[k]=v
    return d
cs="servername=s;dbname=b;username=u;password=p"
print(csdict(cs))                      
