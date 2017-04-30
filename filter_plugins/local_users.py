""" Local Users Ansible Jinja Filters """
from __future__ import print_function
__metaclass__ = type

def passwd_to_dict(passwd_lines):
    """Take a list of lines from a passwd file and convert to python dict"""
    passwd_dict = dict()
    for line in passwd_lines:
        values = line.split(':')
        passwd_dict[values[0]]  = dict()
        passwd_dict[values[0]]['uid'] = int(values[2])
        passwd_dict[values[0]]['gid'] = int(values[3])
        passwd_dict[values[0]]['comment'] = values[4]
        passwd_dict[values[0]]['home'] = values[5]
        passwd_dict[values[0]]['shell'] = values[6]
    return passwd_dict

def passwd_undefined_accounts(passwd, accounts):
    undefined_accounts = dict()
    for user in passwd:
        if user not in accounts:
            undefined_accounts[user] = passwd[user]
    return undefined_accounts

def passwd_managed_uids(passwd, managed_uids):
    managed_passwd = dict()
    for user, val in passwd.iteritems():
        for uid_spec in managed_uids:
            if (uid_spec.has_key('min') and uid_spec.has_key('max') and \
                val['uid'] >= uid_spec['min'] and val['uid'] <= uid_spec['max']) or \
                (uid_spec.has_key('uid') and val['uid'] == uid_spec['uid']):
                    managed_passwd[user] = passwd[user]
    return managed_passwd

def group_to_dict(group_lines):
    group_dict = dict()
    for line in group_lines:
        values = line.split(':')
        group_dict[values[0]] = dict()
        group_dict[values[0]]['password'] = values[1]
        group_dict[values[0]]['gid'] = int(values[2])
        group_dict[values[0]]['users'] = values[3]
    return group_dict

def absent(dictionary):
    """Return local_user_group with only absent state"""
    return {key: val for key, val in dictionary.iteritems()
            if type(val) is dict and 'state' in val
            and val['state'].lower() == 'absent'}

def present(dictionary):
    """Return local_user_group with state of present or undefined"""
    return {key: val for key, val in dictionary.iteritems()
            if type(val) is not dict or 'state' not in val
            or val['state'].lower() == 'present'}


def group_undefined_groups(group, groups):
    undefined_group = dict()
    for grp in group:
        if grp not in groups:
            undefined_group[grp] = group[grp]
    return undefined_group

def group_managed_gids(group, managed_gids):
    managed_group = dict()
    for grp, val in group.iteritems():
        for gid_spec in managed_gids:
            if (gid_spec.has_key('min') and gid_spec.has_key('max') and \
                val['gid'] >= gid_spec['min'] and val['gid'] <= gid_spec['max']) or \
                (gid_spec.has_key('gid') and val['gid'] == gid_spec['gid']):
                    managed_group[grp] = group[grp]
    return managed_group


class FilterModule(object):

    def filters(self):
        return {
            'local_users_passwd_undefined_accounts': passwd_undefined_accounts,
            'local_users_passwd_managed_uids': passwd_managed_uids,
            'local_users_passwd_to_dict': passwd_to_dict,
            'local_users_group_to_dict': group_to_dict,
            'local_users_group_undefined_groups': group_undefined_groups,
            'local_users_group_managed_gids': group_managed_gids,
            'local_users_groups_absent': absent,
            'local_users_groups_present': present,
            'local_users_accounts_present': present,
            'local_users_accounts_absent': absent,
        }
