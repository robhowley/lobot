## lobot

An ansible role that leverages jinja2 macros for reusable CloudFormation templates for some of the most common AWS 
resources. By moving resource deployment out of CloudFormation templates and into an ansible native api 
[lobot](http://starwars.wikia.com/wiki/Lobot) helps you manage your [cloud resources](http://starwars.wikia.com/wiki/Cloud_City)
in a more readable and easy to use way.  

## Install

Using [ansible galaxy](https://galaxy.ansible.com/), add the following to your [requirements.yml](http://docs.ansible.com/ansible/latest/galaxy.html#installing-multiple-roles-from-a-file).

```bash
- src: https://github.com/robhowley/lobot
  scm: git
  version: v0.1.0
```

## Example

To use **lobot** simply import the role and reference the tasks associated with the resources you want to deploy. For 
example, to create a stack that has
  * an S3 bucket 
  * with SNS notifications on object created events 
  * and a read/write managed policy that can be attached to other resources 
you would do the following ...

```bash
- hosts: localhost
  connection: local
  roles:
  - lobot
  
  tasks:
  - include: "{{ lobot.bucket }}"
    vars:
      stack_name: test-bucket-stack
      name: test-bucket
      principal_read_access: "{{ list_principals_who_can_read_by_default }}"
      sns_topics:
        topics:
        - name: ObjectAddedTopic
          event: created
      output_managed_policies:
      - name: ReadWriteListMP
        policy: rwl
      stack_output_prefix: test_

  - debug:
      var: test_lobot_bucket
```
