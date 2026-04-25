# Generative AI: Comprehensive Guide to Prompting and Models

## System Prompt

### Definition
A system prompt is an initial instruction provided to a generative AI model that defines its behavior, personality, and operational constraints. It serves as the foundational context that shapes how the model responds to all subsequent user queries.

### Purpose
- Establish the model's role and expertise area
- Define communication style and tone
- Set boundaries for acceptable responses
- Provide context for specialized domains
- Ensure consistent behavior across conversations

### Example
```
You are an expert software engineer with 10 years of experience in cloud architecture. 
Provide clear, concise technical explanations. Always include code examples when relevant. 
Do not provide financial advice. Focus on best practices and security considerations.
```

### Key Points
- System prompts are processed before user input
- They influence the entire conversation session
- Different tasks require different system prompts
- System prompts should be specific and measurable
- Clear instructions lead to better output quality

---

## Guardrails

### Definition
Guardrails are predefined rules, boundaries, and safety mechanisms that constrain model behavior and prevent unwanted outputs. They act as filters to ensure responses are safe, compliant, and aligned with organizational policies.

### Purpose
- Prevent generation of harmful or inappropriate content
- Ensure compliance with regulations and policies
- Protect user privacy and data security
- Maintain brand consistency
- Filter out sensitive information

### Example
```
- Block responses containing hate speech, violence, or illegal activities
- Redact personally identifiable information (PII)
- Prevent discussion of sensitive financial data
- Reject requests for code that could be used maliciously
- Limit response length to prevent token overflow
```

### Key Points
- Guardrails operate at multiple levels (input, processing, output)
- They can be rule-based or learned through training
- Guardrails reduce model hallucinations
- They are essential for production deployments
- Guardrails should be regularly audited and updated

---

## System Prompt vs Guardrails

### Comparison Table

| Aspect | System Prompt | Guardrails |
|--------|---------------|-----------|
| **Purpose** | Define behavior and role | Enforce safety and compliance |
| **Scope** | Shapes response style | Restricts response content |
| **Implementation** | Part of model input | External filtering mechanism |
| **Flexibility** | Can change per conversation | Typically static |
| **Examples** | Expertise, tone, context | Content filtering, PII redaction |
| **Failure Mode** | Incorrect or off-topic responses | Overly restrictive outputs |
| **User Visibility** | Usually hidden | Transparent when triggered |

---

## GenAI Architecture with Guardrails

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────┐
│                    User Input                           │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│              Input Guardrails                           │
│  ┌─ PII Detection                                       │
│  ├─ Toxicity Check                                      │
│  ├─ Prompt Injection Prevention                         │
│  └─ Input Validation                                    │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│         System Prompt + User Message                    │
│              ↓                                           │
│         Language Model                                  │
│              ↓                                           │
│         Raw Output Generation                           │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│             Output Guardrails                           │
│  ┌─ Content Filtering                                   │
│  ├─ Factuality Check                                    │
│  ├─ PII Redaction                                       │
│  ├─ Harmful Content Detection                           │
│  └─ Response Validation                                 │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│              Final Response                             │
└─────────────────────────────────────────────────────────┘
```

---

## Temperature

### Definition
Temperature is a hyperparameter that controls the randomness or creativity of model outputs. It adjusts the probability distribution of token selection, affecting how deterministic or creative the model's responses are.

### Range
- **0.0**: Deterministic (always selects highest probability token)
- **0.5**: Balanced (some creativity with consistency)
- **1.0**: Standard randomness
- **1.5+**: High creativity and randomness
- **Typical range**: 0.0 to 2.0 (varies by model)

### Example
```
Same prompt, different temperatures:

Temperature: 0.0
Output: "The capital of France is Paris."

Temperature: 0.7
Output: "France's capital city, Paris, is located on the Seine river."

Temperature: 1.5
Output: "In the romantic lands of France, the magnificent Paris stands 
as the beacon of culture and art, serving as the nation's grand capital."
```

### Recommended Usage Table

| Use Case | Temperature | Reason |
|----------|-------------|--------|
| Code generation | 0.0 - 0.2 | Accuracy and consistency |
| Customer support | 0.3 - 0.5 | Accurate with natural variation |
| Creative writing | 0.8 - 1.0 | Balance creativity and coherence |
| Brainstorming | 1.0 - 1.5 | Maximum diversity of ideas |
| Summarization | 0.2 - 0.4 | Factual consistency |
| Q&A systems | 0.1 - 0.3 | Reliable answers |

---

## Top-P (Nucleus Sampling)

### Definition
Top-P (also called nucleus sampling) is a sampling technique that selects from the smallest set of tokens whose cumulative probability exceeds a threshold P. It provides an alternative to temperature by filtering tokens based on probability mass rather than fixed count.

### Example Probability Table

```
Consider these tokens with probabilities for next word:

Token      | Probability | Cumulative
-----------|-------------|------------
"the"      | 0.40        | 0.40
"a"        | 0.25        | 0.65
"this"     | 0.15        | 0.80
"that"     | 0.10        | 0.90
"which"    | 0.05        | 0.95
"another"  | 0.03        | 0.98
"some"     | 0.02        | 1.00

With Top-P = 0.9:
Selected tokens: "the", "a", "this", "that", "which"
(cumulative probability reaches 0.95)

With Top-P = 0.7:
Selected tokens: "the", "a", "this"
(cumulative probability reaches 0.80)
```

### Example Token Selection
```
Top-P = 0.95 (include most likely tokens)
  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░ (95% of probability mass)
  Includes: high probability + some low probability tokens
  Result: Diverse but mostly coherent

Top-P = 0.7 (restrict to core tokens)
  ▓▓▓▓▓▓▓░░░░░░░░░░░░░ (70% of probability mass)
  Includes: only high probability tokens
  Result: More focused and deterministic
```

---

## Temperature vs Top-P

### Comparison Table

| Aspect | Temperature | Top-P |
|--------|-------------|-------|
| **What it controls** | Randomness/sharpness | Probability threshold |
| **Scale** | 0.0 to 2.0+ | 0.0 to 1.0 |
| **0 value** | Deterministic | Very restrictive |
| **1.0 value** | Standard behavior | Diverse sampling |
| **How it works** | Scales logits | Filters by cumulative probability |
| **Best for** | General tuning | Fine-grained quality control |
| **Interaction** | Works independently | Can combine with temperature |
| **Typical usage** | Most common | Often paired with temperature |

---

## Common Production Settings

### Example Configuration Snippet

```yaml
# Production Configuration for Q&A System
model_config:
  temperature: 0.3
  top_p: 0.9
  max_tokens: 512
  top_k: 40

# Production Configuration for Creative Content
creative_config:
  temperature: 0.8
  top_p: 0.95
  max_tokens: 1024
  top_k: 50

# Production Configuration for Code Generation
code_config:
  temperature: 0.2
  top_p: 0.5
  max_tokens: 2048
  top_k: 20

# Production Configuration for General Chat
chat_config:
  temperature: 0.7
  top_p: 0.9
  max_tokens: 512
  top_k: 40
```

---

## Amazon Bedrock

### Overview
Amazon Bedrock is a fully managed service that provides access to a wide range of high-performing foundation models from various AI providers through a single API. It enables organizations to build and scale generative AI applications without managing infrastructure.

### Foundation Models in Bedrock

| Provider | Model | Strengths | Use Case |
|----------|-------|-----------|----------|
| Anthropic | Claude 3 | Advanced reasoning, long context | Complex analysis, coding |
| Meta | Llama 2, Llama 3 | Efficiency, open-source aligned | Cost-effective applications |
| Mistral AI | Mistral 7B, Mixtral | Speed, multilingual support | Fast inference applications |
| Cohere | Command | Text generation, search | Content creation, search |
| Stability AI | Stable Diffusion | Image generation | Visual content creation |
| AI21 Labs | Jurassic-2 | Few-shot learning | Specialized tasks |

### Bedrock Architecture

```
┌─────────────────────────────────────────────────────────┐
│                  User Application                       │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│          Amazon Bedrock API                             │
│  ┌──────────────────────────────────────────────────┐   │
│  │      Bedrock Control Plane                       │   │
│  │  - Model Selection                               │   │
│  │  - Request Routing                               │   │
│  │  - Authentication & Authorization                │   │
│  └──────────────────────────────────────────────────┘   │
└──────────────────────┬──────────────────────────────────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
        ▼              ▼              ▼
┌───────────────┐ ┌───────────────┐ ┌───────────────┐
│ Foundation    │ │ Knowledge     │ │ Agents        │
│ Models        │ │ Bases         │ │               │
└───────────────┘ └───────────────┘ └───────────────┘
        │              │              │
        ▼              ▼              ▼
┌───────────────┐ ┌───────────────┐ ┌───────────────┐
│ Claude        │ │ Vector DB     │ │ Tool Calling  │
│ Llama         │ │ Integration   │ │ Agent Loop    │
│ Mistral       │ │ RAG Pipeline  │ │ Planning      │
└───────────────┘ └───────────────┘ └───────────────┘
```

### Key Features
- **Unified API**: Single interface for multiple foundation models
- **Managed Service**: No infrastructure management required
- **Security**: VPC endpoints, encryption, IAM integration
- **Cost Optimization**: Pay-per-use pricing, batch processing
- **Enterprise Ready**: Compliance, audit logging, high availability
- **Model Customization**: Fine-tuning and prompt engineering tools
- **Integration**: AWS service ecosystem support

---

## Bedrock Components

### Foundation Models
Pre-trained large language and multimodal models provided by leading AI companies. These models can generate text, images, and perform complex reasoning tasks without modification.

**Key aspects:**
- Multiple models with different strengths
- Model switching without code changes
- Regular model updates and new releases
- Performance benchmarks available

### Bedrock Runtime
The core service for invoking foundation models and agents. Handles request processing, streaming responses, and error management.

**Capabilities:**
- Synchronous and asynchronous invocation
- Streaming responses for real-time applications
- Token counting and usage tracking
- Response format consistency across models

### Knowledge Bases
Managed retrieval-augmented generation (RAG) service that integrates external data sources with foundation models. Enables grounding LLM responses in proprietary data.

**Features:**
- Automatic data chunking and embedding
- Vector database integration (e.g., Aurora PostgreSQL pgvector)
- Hybrid search (semantic + keyword)
- Data sync and refresh management

### Bedrock Agents
Autonomous agents that can break down complex tasks, reason about solutions, and interact with external APIs and tools. Implements agentic workflows with planning and memory.

**Capabilities:**
- Automatic planning and task breakdown
- Tool integration and API calling
- Memory management (short and long-term)
- Loop execution with guardrails

---

## Model Customization

### Prompt Engineering
Techniques to optimize prompts for specific tasks without changing model weights. Enables quick iteration and adaptation.

**Methods:**
- Few-shot prompting with examples
- Chain-of-thought prompting for reasoning
- System prompt optimization
- Prompt templating for consistency

### Fine-tuning
Training process that adapts a foundation model to specific domains or tasks using custom datasets. Creates specialized versions for particular use cases.

**Approaches:**
- Supervised fine-tuning with labeled examples
- Continued pretraining on domain data
- Instruction-following optimization
- Parameter-efficient fine-tuning (LoRA, QLoRA)

### Benefits Table

| Customization | Implementation Time | Cost | Performance Gain | Flexibility |
|---------------|-------------------|------|-----------------|-------------|
| Prompt Engineering | Minutes | Free | 10-20% | High |
| Few-shot Prompting | Hours | Minimal | 15-30% | High |
| Fine-tuning | Days-Weeks | Moderate | 30-60% | Medium |
| Continued Pretraining | Weeks | High | 40-80% | Low |

---

## Bedrock vs Traditional ML

### Comparison Table

| Aspect | Amazon Bedrock | Traditional ML |
|--------|----------------|----------------|
| **Model Training** | Pre-trained, no training required | Requires labeled data and training |
| **Time to Production** | Hours to days | Weeks to months |
| **Infrastructure** | Fully managed | Must build and maintain |
| **Expertise Required** | Prompt engineering | Data science + ML ops |
| **Customization** | Prompt and fine-tuning | Full model rebuilding |
| **Scalability** | Auto-scaling included | Manual scaling setup |
| **Cost Model** | Pay-per-use | Infrastructure + compute |
| **Model Updates** | Automatic | Manual retraining |
| **Compliance** | Built-in governance | Custom compliance setup |
| **Integration** | AWS service native | Custom integration |

---

## Summary

Generative AI development on AWS requires understanding several key concepts:

- **System Prompts** guide model behavior and establish context
- **Guardrails** ensure safety, compliance, and quality control
- **Temperature and Top-P** provide fine-grained control over output randomness
- **Amazon Bedrock** abstracts infrastructure complexity with a managed service
- **Foundation Models** provide pre-trained capabilities without training overhead
- **Knowledge Bases** enable grounding responses in proprietary data
- **Bedrock Agents** automate complex multi-step tasks
- **Customization** through prompting and fine-tuning adapts models to specific needs

Start with Amazon Bedrock's managed experience, use prompt engineering for quick iterations, and fine-tune models for specialized domains requiring higher accuracy.

---

## Additional Resources

- Review your specific use case requirements
- Test multiple temperature and Top-P combinations
- Document your system prompts and guardrails
- Monitor model performance in production
- Implement comprehensive logging and monitoring
- Plan for model updates and versioning
- Establish clear governance policies
