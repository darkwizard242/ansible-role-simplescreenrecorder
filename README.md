[![build-test](https://github.com/darkwizard242/ansible-role-simplescreenrecorder/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-simplescreenrecorder/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-simplescreenrecorder/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-simplescreenrecorder/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/d/darkwizard242/simplescreenrecorder) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-simplescreenrecorder&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-simplescreenrecorder) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-simplescreenrecorder&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-simplescreenrecorder) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-simplescreenrecorder&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-simplescreenrecorder) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-simplescreenrecorder?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-simplescreenrecorder?color=orange&style=flat-square)

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

Variable                           | Description
---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------
simplescreenrecorder_app           | Defines the app to install i.e. **simplescreenrecorder**
simplescreenrecorder_desired_state | Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Defaults to `present`.

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

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
