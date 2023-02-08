# Contributing

Hello. This is the place where you can contribute to the Ansible docsite.

We love it when people submit new ideas, make improvements, and fix our mistakes. So welcome!

## Things to know before your first contribution

- All code and doc submissions are done through pull requests against the `devel` branch.
- Take care to make sure no merge commits are in your submission. Use `git rebase` vs `git merge` for this reason.
- We ask all of our community members and contributors to adhere to the [Ansible code of conduct]. If you have questions, or need assistance, please reach out to our community team at [codeofconduct@ansible.com].

## Building the docsite locally

Test your changes to the Ansible docsite.

```bash
$ pip install -r requirements.txt
$ python build.py
```

[Ansible code of conduct]: http://docs.ansible.com/ansible/latest/community/code_of_conduct.html
[codeofconduct@ansible.com]: mailto:codeofconduct@ansible.com
