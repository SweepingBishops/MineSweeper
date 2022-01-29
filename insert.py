
 def  addhighscore(gridsize,username,time):   
    import mysql.connector as mycon
    conn=mycon.connect(host='localhost',user="root",password="computer",charset = "utf8",database="hs")
    cur=conn.cursor()
    cur.execute(f"insert into gridsize{gridsize} values( '{username}','{time}')")
    conn.commit()

