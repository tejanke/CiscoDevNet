Review
* dictionary
* import statements
  * from something import something_else
    * import something_else only
  * import something
    * import everything
  * tabulate
  * operator, itemgetter
  * pprint
  * lists
    * a = list()
    * a = []
    * not naturally sorted
    * they maintain order
    * to sort them use sorted()
      * print(tabulate(sorted(devices, key=itemgetter("vendor", "os", "version")), headers="keys"))
  * for loops
  * devices
    * create an empty list to hold devices
    * create a dictionary for each device, append it to the devices list