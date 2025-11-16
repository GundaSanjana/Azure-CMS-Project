# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*
a) Virtual Machine (VM)

Cost:
A VM is billed like a full server: you pay for the selected size (CPU, RAM, storage) as long as it’s allocated, regardless of how busy the app is. For this CMS, a small VM like Standard B1ls is enough, but the cost is still higher than a free or low-tier App Service plan, especially if I forget to stop or delete the VM. I would also be responsible for managing OS patches and any extra software, which indirectly adds “operational cost” in terms of my time.

Scalability:
A single VM scales vertically: to handle more load, I’d have to resize it to a bigger SKU or manually add more VMs behind a load balancer. This is more complex to manage and usually requires planning and downtime. Auto-scaling is possible, but I have to configure it explicitly using scale sets or other Azure services.

Availability:
VM availability depends on how I configure it. A single VM has a single point of failure. To achieve higher availability, I’d need multiple VMs in an availability set or zone, plus a load balancer. I am responsible for OS updates, security patches, and restarts, which can cause downtime if not handled carefully.

Workflow:
Using a VM gives me full control over the OS and runtime stack. I can install any version of Python, configure Nginx/Gunicorn manually, and host other services on the same machine. However, deployment is more manual: SSH into the VM, clone the GitHub repo, create a virtual environment, install dependencies, configure Nginx, and manage services. This provides flexibility but also increases complexity and maintenance effort.

b) App Service (Web App)

Cost:
App Service offers a Free F1 tier, which is ideal for this project and development scenarios. I don’t pay for idle VMs directly; instead, I pay per App Service plan, which can host multiple web apps. For small workloads like this article CMS, the free or basic tiers are cheaper than running a dedicated VM 24/7. Scaling up to higher tiers is still generally cost-effective compared to managing multiple VMs myself.

Scalability:
App Service has built-in horizontal scaling. I can increase the number of instances with a slider or configure auto-scale rules based on CPU, memory, or schedule. It abstracts away the individual servers, so I don’t have to manage the underlying OS. This makes it easier to handle traffic spikes and future growth of the CMS without re-architecting the deployment.

Availability:
App Service is a managed platform (PaaS), so Microsoft handles OS patching, infrastructure redundancy, and many aspects of uptime. The service is integrated with Azure’s availability features, and I can choose higher tiers with built-in SLA guarantees. I don’t need to manually set up multiple machines or a load balancer just to get a highly available endpoint.

Workflow:
The developer workflow with App Service is very streamlined. I can connect the App Service to GitHub via Deployment Center so that pushes to a branch automatically deploy to Azure. Configuration like connection strings and secrets can be stored in Application Settings rather than hard-coded in the code. I don’t manage the OS, web server, or runtime directly; I only focus on the app code and settings. This reduces operational overhead and speeds up development.

### VM or App Service? (and why):

For this project, I chose to deploy the Flask CMS using Azure App Service (Web App).

The main reasons are:

Cost – The App Service free tier is enough for this small CMS, so I don’t pay for a dedicated VM. It’s more economical for a learning project and small workloads.

Simplicity & Workflow – App Service gives me an easy deployment pipeline via GitHub and a simple configuration experience through Application Settings. I don’t have to manage the OS, patching, or web server directly, which lets me focus on the Flask app itself.

Built-in scalability & availability – If the CMS ever needs to handle more users or traffic, I can scale up or out using the App Service plan without redesigning the infrastructure or manually configuring load balancers and extra VMs.

Because of these factors, App Service is a better fit for this application than a VM for my current needs.

### Assess app changes that would change your decision.

If the CMS application changed in ways that demanded more low-level infrastructure control, my choice might switch toward a VM (or even a container-based solution). For example, if I needed custom OS-level software, unusual networking requirements, or background services that App Service doesn’t support easily, a VM would give me full control to install and configure everything exactly as needed.

Similarly, if the application expanded into a multi-component system (e.g., additional microservices, custom message queues, or specialized database engines) that needed tight control over the environment and network topology, managing everything on VMs (or using containers orchestrated by services like AKS) might become more suitable. In that case, I would accept the extra operational complexity of VMs in exchange for the flexibility they provide.

Right now, though, the CMS is a straightforward web app that primarily needs a Python runtime, connection to Azure SQL and Blob Storage, and an OAuth2 login flow. For that scenario, App Service remains the most practical and maintainable option.