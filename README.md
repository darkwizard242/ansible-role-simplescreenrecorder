[![Build Status](https://travis-ci.com/darkwizard242/ansible-role-simplescreenrecorder.svg?branch=master)](https://travis-ci.com/darkwizard242/ansible-role-simplescreenrecorder) ![Ansible Role](https://img.shields.io/ansible/role/42038?color=dark%20green) ![Ansible Role](https://img.shields.io/ansible/role/d/42038?color=dark&style=flat-square) ![Ansible Quality Score](https://img.shields.io/ansible/quality/42038?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-simplescreenrecorder&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-simplescreenrecorder) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-simplescreenrecorder?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-simplescreenrecorder?color=orange&style=flat-square)

# Ansible Role: simplescreenrecorder

Role to install (_by default_) [SimpleScreenRecorder](https://github.com/MaartenBaert/ssr) package or uninstall (_if passed as var_) on **Debian** based and **EL** based systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
simplescreenrecorder_app: simplescreenrecorder
simplescreenrecorder_desired_state: present
```

### Variables table:

Variable                           | Value (default)      | Description
---------------------------------- | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------
simplescreenrecorder_app           | simplescreenrecorder | Defines the app to install i.e. **simplescreenrecorder**
simplescreenrecorder_desired_state | present              | Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Defaults to `present`.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **simplescreenrecorder** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.simplescreenrecorder
```

For customizing behavior of role (i.e. installation of latest **simplescreenrecorder** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.simplescreenrecorder
  vars:
    simplescreenrecorder_desired_state: latest
```

For customizing behavior of role (i.e. un-installation of **simplescreenrecorder** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.simplescreenrecorder
  vars:
    simplescreenrecorder_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-simplescreenrecorder/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
