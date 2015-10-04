# Database Types
- Google App Engine has a Number of different options for the types of the properties of an entity (i.e. in SQL Language: the columns of our table)
- Some of the popular ones are:
	- Integer - for storing integers
	- Float - for floating point numbers
	- String - for storign Strings (must be under 500 characters and can be indexed)
	- Text - can be >500 chars and it CANNOT be indexed, hence we can't sort based on a text property.
	- Date - for storing dates
	- Time - for storing times
	- DateTime - for storing both, date and times
	- Email
	- Link
	- Postal Address
	etc.