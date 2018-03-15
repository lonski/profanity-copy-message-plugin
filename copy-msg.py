"""
Copies chat messages to clipboard.
"""

import prof
from collections import deque
import pyperclip

history_len: 20
messages = {}

def prof_init(version, status, account_name, fulljid):
    synopsis = [
        "/copy",
        "/copy <message index>"
    ]
    description = "Copies message content to clipboard"
    args = [
        [ "<message index>", "Defines which message to copy (if not the latest)" ]
    ]
    examples = [
        "/copy",
        "/copy -1"
    ]
    prof.register_command("/copy", 0, 1, synopsis, description, args, examples, _cmd_copy)
    prof.cons_show("Command '/copy' registered successfully.")

def prof_post_chat_message_display(barejid, resource, message):
    _add_message(barejid, message)

def _add_message(jid, message):
    l = _get_messages(jid)
    l.appendleft(message)
    if len(l) > history_len:
        l.pop()

def _get_messages(jid):
    if not jid in messages:
        messages[jid] = deque([])
    return messages[jid]

def _cmd_copy(msg_index):
    if msg_index is None:
        msg_index = 0
    else:
        msg_index = int(msg_index)

    jid = prof.get_current_recipient()
    msg_list = _get_messages(jid)

    if abs(msg_index) >= len(msg_list):
        prof.chat_show(jid,"Error: message with that index is not stored and cannot be copied to clipboard.")
        return

    msg = msg_list[int(msg_index)]
    pyperclip.copy(msg)
    prof.chat_show(jid, "Copied message '" + msg + "'.")

