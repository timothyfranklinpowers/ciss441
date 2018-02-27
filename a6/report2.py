import sqlite3

dbfile = 'payroll_dc_small.db' #the database file
conn = sqlite3.connect(dbfile) #connect to the database

print ("Opened database for report 2 successfully")

def main():

    print("{0:<20} {1:<15} {2:<10} {3:<10}".format(
    "agelvl", "occtypt", "salmax", "salmin"
    ))

    cursor = conn.execute("""
        select agelvl.agelvlt, occ.occtypt ,max(f.salary) salmax, min(f.salary) salmin
        from factdata_mar2016 f, agelvl, occ
        where f.agelvl=agelvl.agelvl AND f.occ=occ.occ
        group by agelvl.agelvlt, occ.occtypt
        order by agelvlt asc
        limit 20;
    """)
    for row in cursor:
        agelvlt, occtypt, salmax, salmin = row
        print("{0:<20} {1:<15} {2:<10} {3:<10}".format(
        agelvlt,
        occtypt,
        salmax,
        salmin))

        conn.commit()

print("This is Tim's report on occupation types and the age range associated with high/low salaries.")

if __name__ == "__main__":
    main()
