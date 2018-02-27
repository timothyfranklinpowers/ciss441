import sqlite3

dbfile = 'payroll_dc_small.db' #the database file
conn = sqlite3.connect(dbfile) #connect to the database

print ("Opened database for report 3 successfully")

def main():

    print("{0:<30} {1:<20} {2:<12} {3:<12} {4:<30}".format(
    "Supervisor", "Supervisor Type", "Max Salary", "Min Salary", "Work Status"
    ))

    cursor = conn.execute("""
        select super.supervist, super.supertypt, max(f.salary) salmax, min(f.salary) salmin, wkstat.workstatt
        from factdata_mar2016 f, super, wkstat
        where f.supervis=super.supervis AND f.workstat=wkstat.workstat
        group by super.supervist, super.supertypt
        order by super.supervist asc
        limit 20;
    """)
    for row in cursor:
        supervist, supertypt, salmax, salmin, workstatt = row
        print("{0:<30} {1:<20} {2:<12} {3:<12} {4:<30}".format(
        supervist,
        supertypt,
        salmax,
        salmin,
        workstatt))

        conn.commit()

print("This is Tim's report on high/low salaries based on location.")

if __name__ == "__main__":
    main()
