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
  version: v1.0.0
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
  
  tasks:
  - include_role:
      name: lobot/bucket
    vars:
      bucket:
        bucket_name: some-test-bucket-12342314
        sns_topics:
          topics:
          - resource_name: TestSnsTopic
            name: dev-test-sns-topic
            event: s3:ObjectCreated:*
        create_read_managed_policy: 'true'
        create_write_managed_policy: 'true'

  - debug:
      var: lobot_stacks
```
