# ANTLR4 example with python3 runtime

Command to build from grammar in Linux (assuming you have antlr4 as the alias for antlr4 java binaries):

```
antlr4 -Dlanguage=Python3 arithmetic.g4
```

This will generate the lexer and parser files that are already included in this repository.

In case you trust the source of the .py files / are too lazy to download antlr / just want to run this test, skip above and follow :

### For environment creation:
``` 
mkvirtualenv -p /usr/bin/python3 py3env
pip install antlr4-python3-runtime 
```

### To see the output
```
python main.py < infile
```

The output should look like ``` Parsed expression 3*3-2+2*2 has value 11 ```

### Removing the environment
```
rmvirtualenv py3env
```
You can skip the creation of virtual environments if you know what you are doing.

Courtesy : 
http://blog.anvard.org/articles/2016/03/29/antlr-python-arithmetic.html