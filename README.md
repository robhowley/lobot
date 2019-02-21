[![release](https://img.shields.io/github/release/robhowley/lobot.svg)](https://github.com/robhowley/lobot/releases)

# lobot: deploy aws resources with ansible

An ansible role that leverages jinja2 macros for reusable CloudFormation templates for some of the most common AWS 
resources. By moving resource deployment out of CloudFormation templates and into an ansible native api 
[lobot](http://starwars.wikia.com/wiki/Lobot) helps you manage your [cloud resources](http://starwars.wikia.com/wiki/Cloud_City)
in a more readable and easy to use way.  

## Install

Using [ansible galaxy](https://galaxy.ansible.com/), either add the following to your 
[requirements.yml](http://docs.ansible.com/ansible/latest/galaxy.html#installing-multiple-roles-from-a-file)

```bash
- src: https://github.com/robhowley/lobot
  scm: git
  version: v1.0.0
```

or run
```bash
ansible-galaxy install robhowley.lobot
```

## Example

To use **lobot** simply import the role and reference the tasks associated with the resources you want to deploy. For 
an example with some actual substance to it, to deploy
  * an S3 bucket 
  * with SNS notifications on [object created](https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html#notification-how-to-event-types-and-destinations) 
  events 
  * and a managed policy with [read access](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazons3.html#amazons3-actions-as-permissions) 
  to the bucket that can be attached to other resources
  * an SQS queue subscribed to the topic
  * and a dead letter queue that stores messages received 5 times
you would do the following ...

```bash
- hosts: localhost
  connection: local
  
  tasks:
  - set_fact:
      bucket_name: some-test-bucket-12342314
      queue_name: sample-queue-134324
      
  - include_role:
      name: lobot/bucket
    vars:
      bucket:
        bucket_name: "{{ bucket_name }}"
        sns_topics:
          topics:
          - name: dev-test-sns-topic
            output_name: TestSnsTopic
            event: s3:ObjectCreated:*
        create_read_managed_policy: true
        
  # use the autogenerated stack info in the lobot_stacks variable 
  # to subscribe to the new s3 object topic in your new queue
  - include_role:
      name: lobot/queue
    vars:
      queue:
        queue_name: "{{ queue_name }}"
        subscribe_to_sns_topic_arn: "{{ lobot_stacks[bucket_name].stack_outputs.TestSnsTopic }}"
        redrive_policy_max_receive_count: 5
        
  # view all of your created stacks here      
  - debug:
      var: lobot_stacks
```

## Other role info

### Role variables
There is a single *role level configuration variable* with the following default 
```
lobot_keep_it_quiet: false
```
This variable is passed to `no_log` where appropriate. Setting this to true will suppress logs generated by the ansible 
modules used in the role.

Each time a resource is deployed a *role level output variable* `lobot_stacks` is updated with the new stack info.
```bash
lobot_stacks: (dict)
    [name_of_resources_deployed]: [output of the cloudformation module]
```
The `lobot_stacks` variable is particularly useful because it will provies easy access to output stack variables.

### Dependencies
None. Keep it simple.

### Requirements
Ansible 2.4 or above
