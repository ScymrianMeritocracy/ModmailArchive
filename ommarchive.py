#!/usr/bin/env python3

import collections
import os
import pathlib
import praw
import ruamel.yaml

def archive(r):
    """Export old Reddit modmail threads to YAML."""
    mypath = os.path.dirname(os.path.realpath(__file__))
    pathlib.Path(f"{mypath}/archives").mkdir(exist_ok=True)
    for sub in r.redditor(r.config.username).moderated():
        perms = []
        for mod in sub.moderator():
            if mod == r.config.username:
                perms = mod.mod_permissions
                break
        if "mail" not in perms and "all" not in perms:
            continue
        mydata = collections.OrderedDict()
        myfile = f"{mypath}/archives/{sub.display_name}.yaml"
        for msg in sub.mod.inbox(limit=None):
            tree = {}
            tree["op"] = [msg]
            for child in msg.replies:
                if child.parent_id in tree.keys():
                    tree[child.parent_id].append(child)
                else:
                    tree[child.parent_id] = [child]
            pl = f"https://old.reddit.com/message/messages/{msg.id}"
            mydata[pl] = [msg.subject]
            mydata[pl].append(readmsg(msg, tree))
        with open(myfile, "w") as export:
            ruamel.yaml.YAML().dump(mydata, export)

def readmsg(msg, tree):
    """Append the next message in the working dictionary."""
    nextmsg = [msg.author.name, msg.created_utc, msg.body]
    if msg.name in tree.keys():
        for reply in tree[msg.name]:
            nextmsg.append(readmsg(reply, tree))
    return nextmsg

if __name__ == "__main__":
    archive(praw.Reddit())
