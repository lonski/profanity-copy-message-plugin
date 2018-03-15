# Copy message to clipboard

[Profanity](http://www.profanity.im) plugin for copying messages to clipboard. 

## Installation

Install `pyperclip` python module:

```bash
pip install pyperclip
```

Download copy-msg.py and install it in profanity console:

```
/plugins install <path to copy-msg.py>
/plugins load copy-msg.py
```

## Usage

#### Synopsis

```
/copy
/copy <message index>
```

#### Arguments

message_index : Defines which message to copy (if not the latest)
 
#### Examples

Copy the latest message:
```
/copy
```

Copy one before last message:
```
/copy -1
```
