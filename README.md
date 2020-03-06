# Secure Istio Manifests

Helm-managed Istio manifests that provide namespace and deployment specific security to Kubernetes.

**What It Does**

_Deployments & Services_
* Deploys a service and two versions of a UI ('master' and 'test').
* Creates services in front of the service/UI deployments, exposing their ports to inside the Kubernetes cluster..

_Virtual Services & DestinationRules_
* Defines DesinationRules for hosts and 'version' label allow VirtualService-level rules to be applied.
* Defines VirtualServices for each the service and UI (with the UI having traffic percentages being defined for the different versions)

_mTLS, Zero Trust, and Exceptions_
* Enables mTLS across an entire namespace.
* Enforces zero-trust by disallowing all traffic within the namespace.
* Creates principal-based exceptions of zero-trust to allow communication between the UI and backend service.

_Ingress_
* Creates an Istio Ingress Gateway to allow for monitoring and route rules to be applied to external traffic entering the cluster.

**Where Do I Look**

For Istio manifests, check out `chart/templates`.

For service code, check out `src/service`.

For UI code, check out `src/ui`.

**Deploying the Helm Chart**

_NOTE: It's advised to use Helm 2+ when using Istio, as Istio is not fully supportive of Helm 3 yet._

1. Update any values necessary in `chart/values.yaml`.

2. For initial install, run: `helm install secure-istio chart`

3. For updates/upgrades, run: `helm upgrade secure-istio chart`

### Validation and Mutating Webhooks

This project provides a single image and Helm chart that does the following:
1. Image contains both an admission and mutating webhook to ensure A) No privileged escalation in pods or deployments and B) the container runs as a random UID that is in the 'root' (0) group.
    * With a single image, it is a single Kubernetes service that the webhooks can refer to.
2. The helm chart deploys both the validation and mutating webhooks into your environment.
    * It also manages the certificates required for TLS communication to the validation/mutating container.