
def  addhighscore(gridsize,username,time):   
    import mysql.connector as mycon
    conn=mycon.connect(host='localhost',user="roshan",password="Wtmld0w3@lh3?0",charset = "utf8",database="minesweeper")
    cur=conn.cursor()
    cur.execute(f"insert into gridsize{gridsize} values('{username}','{time}')")
    conn.commit()

