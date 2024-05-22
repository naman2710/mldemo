import re

# Read the description.md file
with open('description.md', 'r') as file:
    description = file.read()

# Define a simple function to extract tools and components
def extract_component(description, keyword):
    pattern = re.compile(rf'{keyword} (.*?)(,|\.|\n)', re.IGNORECASE)
    match = pattern.search(description)
    return match.group(1).strip() if match else None

# Extract components from the description
cloud_provider = 'Azure' if 'Azure' in description else 'AWS'
ci_cd_tool = extract_component(description, 'CI/CD pipeline is managed by')
container_registry = extract_component(description, 'pushes Docker images to')
container_orchestration = extract_component(description, 'orchestrating the containers')
config_management = extract_component(description, 'Configuration management is handled by')
infra_provisioning = extract_component(description, 'infrastructure provisioning is done using')

# Generate the PlantUML content
plantuml_content = f"""
@startuml
node "{cloud_provider} Cloud" {{
    node "CI/CD Server" {{
        [{ci_cd_tool}]
    }}
    node "Container Registry" {{
        [{container_registry}]
    }}
    node "Kubernetes Cluster" {{
        node "Kubernetes Master Node" {{
            [K8s Master]
        }}
        node "Kubernetes Worker Node 1" {{
            [Microservice 1]
            [Microservice 2]
        }}
        node "Kubernetes Worker Node 2" {{
            [Microservice 3]
        }}
    }}
    node "Config Management Server" {{
        [{config_management}]
    }}
    node "Infra Provisioning Server" {{
        [{infra_provisioning}]
    }}
}}
@enduml
"""

# Write the PlantUML content to diagram.puml
with open('diagram.puml', 'w') as file:
    file.write(plantuml_content)