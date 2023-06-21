# Invoking modules as scripts
> python -m module [arg]  


#### Non-interactive mode

```shell
python3.11 -m <MODULE_NAME> <ARGUMENT_VALUE>
```
e.g: invoke from the <PROJECT_ROOT_DIR>/python_interpreter directory
```shell
python3.11 -m interactive_module "test argument"
```
OUTPUT
```text
The argument is: test argument
```

#### Interactive mode

```shell
python3.11 -i -m <MODULE_NAME> <ARGUMENT_VALUE>
```

```text
>>> interactive_module_function(<ARGUMENT_VALUE>)
```

e.g.:
```shell
python3.11 -i -m interactive_module "test argument 1"
```
OUTPUT
```text
The argument is: test argument 1
>>> 
```
---

```text
>>> interactive_module_function("test argument2")
```
OUTPUT
```text
The argument is: test argument2
```