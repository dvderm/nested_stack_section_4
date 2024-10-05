#!/usr/bin/env python3
import os

import aws_cdk as cdk

from nested_stack_section_4.nested_stack_section_4_stack import NestedStackSection4Stack
from nested_stack_section_4.network_stack import NetworkStack


app = cdk.App()

root_stack = cdk.Stack(app, 'RootStack')                    # Creating a root stack. Set scope to app variable, to create it under your CDK app. Instead of creating your root stack in app.py, you can also define your root stack as a seperate class file (just like network_stack.py, but then e.g. root_stack.py), and move the nested stack definitions to that file. 

network_stack = NetworkStack(root_stack, 'NetworkStack')    # Changing scope of the nested stacks to the root_stack instead of to the CDK app: NetworkStack(root_stack...) instead of NetworkStack(app...)

NestedStackSection4Stack(root_stack, "NestedStackSection4Stack",  # Changing scope of the nested stacks to the root_stack instead of to the CDK app: NestedStackSection4Stack(root_stack...) instead of NestedStackSection4Stack(app...)
                         my_vpc=network_stack.vpc)

app.synth()
