def function_print_pattern(rows,columns):

    for i in range(rows*2+1):
        for j in range(columns):
            if (i == 0):
                if (j % 2 == 0):
                    print(" ___", end="")
                else:
                    print("    ", end="")
            elif (i % 2 != 0):
                if (j == 0):
                    print("/", end='')
                elif ((i + j) % 2 == 0):
                    print("   ", end="")
                else:
                    print("\___/", end="")
                    if (j == columns-1):
                        print("   \ ", end='')
            else:
                if (j % 2 == 0):
                    print("\___/", end="")
                else:
                    print("   ", end="")

        print()

rows=int(input("Enter no.of rows: "))
columns=int(input("Enter no.of columns: "))
function_print_pattern(rows, columns)
