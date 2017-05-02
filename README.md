LOCAL_USERS
===========

Manage the local users and groups on a system. 

This role by default will removed any users and groups not configured for the system within the user (non system) uid 
and gid range. This behaviour can be changed to not automatically remove users and groups or to manager more uids and
gids.

Requirements
------------

Ansible 2.0+.

Role Variables
--------------

### Main Role Variables

* `local_users_state`: Action for the role to take.
  * _managed_ (default): Managed all users and groups on the system, removing absent users or groups.
  * _present_: Managed only users and groups in configuration.

### User Configuration Variables

* `local_users_accounts`: A dictionary of usernames which wraps the ansible user module.
  * `password`
  * `comment`
  * `expires`
  * `group`
  * `groups`
  * `home`
  * `uid`
  * `gui`
  * `shell`
  * `system`
  * `state`

* `local_users_managed_uids`: A list of dicts to specify the uid range of users to manage. 
                              Remove users not configured in the specifed uid ranges.
    * Defaults: (Min: 1000, Max: 60000)
  * _min_,_max_: Specify a range of uids to manage
  * _uid_: Speicify a single uid to manage


### Group Configuration Variables

* `local_users_groups: A dictionary of groups which wrap the ansible group module
  * `gid`
  * `system`

* `local_users_managed_gids`: A list of dicts to specify the gid range of groups to manage. 
                              Remove groups not configured in the specifed gid ranges.
    * Defaults: (Min: 1000, Max: 60000)
  * _min_,_max_: Speicify a range of guids to manage
  * _gid_: Specify a single gid to manage


Dependencies
------------

None

Example Playbook
----------------

User exists with password.

    - hosts: servers
      roles:
         - { role: brightlingmeuk.local_users,
             local_users_accounts: {user1: {password: '$6$qMYw0rrjWP37S7dL$oWE9LwPIeDiJ5ICVdWeF/1BaJKyWaoJA4oAmWyX.BO6TyAM4IAWUZW4WNWyZdcIoLNxIa2j8TWGldvtiCWfKp/'}}

User doesn't exist.

    - hosts: servers
      roles:
         - { role: brightlingmeuk.local_users,
             local_users_accounts: {user1: {state: 'absent'}}

system uid and gid in management range, don't remove root user.

    - hosts: servers
      roles:
         - { role: brightlingmeuk.local_users,
             local_users_managed_uids: [{min: 0, max: 999}],
             local_users_managed_gids: [{min: 0, max: 999}],
             local_users_accounts: {root: },
             local_users_groups: {root: }}


License
-------

GPLv3

Author Information
------------------

- Robert White | [e-mail](mailto:sentryveil00@gmail.com) | [GitLab](https://gitlab.com/brightling)
