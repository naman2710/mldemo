import argparse

# Parse input arguments
parser = argparse.ArgumentParser(description='Generate PlantUML file.')
parser.add_argument('--cloud-provider', required=True, help='Cloud provider (e.g., AWS, Azure)')
parser.add_argument('--ci-cd-tool', required=True, help='CI/CD tool')
parser.add_argument('--container-registry', required=True, help='Container registry')
parser.add_argument('--container-orchestration', required=True, help='Container orchestration tool')
parser.add_argument('--config-management', required=True, help='Configuration management tool')
parser.add_argument('--infra-provisioning', required=True, help='Infrastructure provisioning tool')
args = parser.parse_args()

# Generate the PlantUML content
plantuml_content = f"""
@startuml
node "{args.cloud_provider} Cloud" {{
    node "CI/CD Server" {{
        [{args.ci_cd_tool}]
    }}
    node "Container Registry" {{
        [{args.container_registry}]
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
        [{args.config_management}]
    }}
    node "Infra Provisioning Server" {{
        [{args.infra_provisioning}]
    }}
}}
@enduml
"""

# Write the PlantUML content to diagram.puml
with open('diagram.puml', 'w') as file:
    file.write(plantuml_content)
