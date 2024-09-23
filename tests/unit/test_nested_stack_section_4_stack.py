import aws_cdk as core
import aws_cdk.assertions as assertions

from nested_stack_section_4.nested_stack_section_4_stack import NestedStackSection4Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in nested_stack_section_4/nested_stack_section_4_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = NestedStackSection4Stack(app, "nested-stack-section-4")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
