# Asteroidea

The Successor to C\*

This programming language is a direct upgrade of C\* (documentation [here](https://github.com/archaversine/cstar)).
Many of the core operations maintain the same behavior, however some have been removed, some have been upgraded,
and new operators have been updated entirely.

Asteroidea makes use of an actual lexer and parser, allowing it to handle much more complex syntax than what was
possible with C\*. Asteroidea also has a new visualization tool, making it easier to see what is happening on the tape
for easier debugging.

## Changes

### Removed Operations

The Following operations have been removed and cannot be used in Asteroidea:

```
%%
C?
E?      // Will eventually be added back
<--     // Will eventually be added back
{}
{{}}
...     // Will eventually be added back (with different implementation)
"       // Was implemented differently
```


### Upgraded Operations

The syntax of many of the remaining operators has changed slightly. However, all operators now have the ability
to handle more complex syntax.

#### Tape Operator (#)

The original syntax of the tape operator remains unchanged. However, it can be used in more ways to set the 
cell values on the tape:

Set the tape to consist of 50 cells all set to the value of 4:

``` 
## 50 4
```

Set the tape to the bytes of a string:

``` 
#"this is a string!"
```

Set the tape to the bytes of a file:

```
#f "my_file.txt"
```

#### Loops and Conditional Statements

Loops and conditional statements are now able to be nested within each other:

```
??(-> ??(+1 <-) <-)
```

Loops can now take in values of other cells and variables instead of needing to be hard coded:

```
[^^myCell](+1)
[$myVar](+1)
```

The syntax for both loops and conditional statements now allows for chaining:

```
[3][3][3]+1     // Same as: [3]([3]([3](+1)))
```

#### Bookmarks

The syntax for `@` and `^` as not changed. Instead, built in bookmarks that automatically update
have been added:

```
__current   // Bookmark to currently selected cell
__first     // Bookmark to first cell of tape
__last      // Bookmark to last cell on tape
```

#### Functions

The syntax for functions has been significantly upgraded. The original C* syntax for functions
is still used, but functions can now be nested, and take in parameters.

Function parameters must always be a number, and are accessed inside the function with the new `$` operator.
This means that functions can take in a hard coded number, the value of a cell, or the value of a variable
when called.

A function that adds the parameter `x` to the current cell:

```
&add<x>(+$x)    // Defining the function
*add<4>         // Calling the function (adding 4 to cell)
```

A function that takes in three parameters `x`, `y`, and `z`, that adds `x`, subtracts `y`, and adds `2`
`z` times:

```
&my_func<x, y, z>(+$x -$y [$z]+2)
```

A function passing its parameters to another function:

```
&add<x, y>($+x $+y)
&add_and_move<a, b>(*add<$a, $b> ->) // NOTE: It would not matter if a and b were instead x and y
```

Asteroidea also supports polymorphism, meaning that you can define multiple functions with the same name
that take in different numbers of parameters.

Polymorphism in action:

```
&add<a, b>(~$a ++ $b)
&add<a>(+$a)
&add(+1)

*add<1, 2>
*add<3>
*add
```

#### Importables

The Syntax for `&&` has changed:

```
&& "myfile.csr"
```

With imports, each file has it's own tape and is not transferred to the importing file. However,
all functions and variables declared in any file wll be transferred to the importing file.

### New Operators

#### Variable Assignment Operator [`:=`]

Variables that hold a number type can be declared in a program with the following syntax:

```
my_var := 3                     // Store 3
my_other_var := ^^__current     // Store the value in the bookmarked cell
copy_of_my_var := $my_var       // Store the value in my_var
```

Variables declared inside functions are not accessible from outside the function.

#### Variable Increase and Decrease operators [`+=`] and [`-=`]

Aside from assigning variables, the values of existing variables can be increased and decreased without
the need to export the value somewhere else and reload it back to the variable with `:=`. Variables can
only be increased/decreased by numbers.

Increasing a variable:

```
my_var := 0

my_var += 3
my_var += $my_other_var
my_var += ^^my_cell
```

Decreasing a variable:

```
my_var := 0

my_var -= 3
my_var -= $my_other_var
my_var -= ^^my_cell
```

#### Variable Lookup Operator [`$`]

The `$` can be used to retrieve the value of something. It can retrieve a variable declared with `:=` or
the value for a parameter in a function.

Getting a value from a value stored with `:=`:

```
my_var := 3

+$my_var    // Adds the value of my_var to the current cell
```

#### Normalize Operator [`| |`]

When creating functions that rely heavily on logical expressions, the `| |` operator is very useful.
It can be applied to any number type, and will return either a `0` if the cell's value is `0` otherwise
it will return `1`.

Normalizing regular numbers:

```
+|88| // Adds 1 to the current cell
+|0|  // Adds 0 to the current cell
```

It can also be applied to anythign of the number type:

```
+|$my_var|
+|^^my_cell|
```

#### Add and Subtract Operator [`++`] and [`--`]

This allows for easy combinations of numbers without the need to do arithmatic in the tape and reload it back
somewhere else.

Adding numbers together:

```
1 ++ 1

1 ++ 2 ++ 3
```

Subtracting numbers:

```
1 -- 1

1 -- 2 -- 3
```

Adding and Subtracting numbers:

```
1 ++ 3 -- 1 ++ 2
```

### Out String Operators

To make printing information to the terminal easier, you can surround text with two backticks (\`). Note:
This will not automatically end a newline, but you can add in newlines using `\n`.

Printing `Hello, World!` to the terminal using an out string:

```
`Hello, World!\n`
```

#### Debug Operators [`[===]`] and [`[%%%]`] 

Two new operators have been added to make debugging code easier. These two operators print the contents of the
tape to the terminal in a much more neat way, and even show the current cell.

For example, the following code:

```
#"Hello, World!"

[===]

[3]->

[%%%]
```

Outputs:

```
        ▼                                                   
─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────
     │  H  │  e  │  l  │  l  │  o  │  ,  │     │  W  │  o  │ ... 
─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────
        ▲                                                   
                          ▼                                 
─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────
     │  72 │ 101 │ 108 │ 108 │ 111 │  44 │  32 │  87 │ 111 │ ... 
─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────
                          ▲                                 
```

#### Halt Operator [`H`]

Halts the program and exits safely.

Halt if the current cell is not equal to `0`:

```
??~H
```

### New Concepts

#### Number type

Anything that requires a number to do something uses a number type. The following are different types of numbers:

```
0           // Regular number
88          // Regular number
^^my_cell   // Number inside bookmarked cell
$my_var     // Number inside variable
|6|         // 'Normalized' number (returns 1 or 0)
'e'         // ASCII value of 'e' (101)
```

These operations can also be chained together:

```
|^^my_cell| // 'Normalizes' value in bookmarked cell
|$my_var|   // 'Normalizes' value in variable
|88|        // 'Normalizes' 88
```

Number types can be added together useing the `++` operator

```
1 ++ 1
|$my_var ++ ^^my_cell| ++ 3
```

Number types can be subtracted from each other using the `--` operator

```
5 -- 3
$my_var -- |^^my_cell|
```
