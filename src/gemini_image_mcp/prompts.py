###############################
# Image Transformation Prompt #
###############################
def get_image_transformation_prompt(prompt: str) -> str:
    """Create a detailed prompt for image transformation.
    
    Args:
        prompt: text prompt
        
    Returns:
        A comprehensive prompt for Gemini image transformation
    """
    return f"""You are an expert image editing AI. Please edit the provided image according to these instructions:

EDIT REQUEST: {prompt}

IMPORTANT REQUIREMENTS:
1. Make substantial and noticeable changes as requested
2. Maintain high image quality and coherence 
3. Ensure the edited elements blend naturally with the rest of the image
4. Do not add any text to the image
5. Focus on the specific edits requested while preserving other elements

The changes should be clear and obvious in the result."""

###########################
# Image Generation Prompt #
###########################
def get_image_generation_prompt(prompt: str) -> str:
    """Create a detailed, Gemini-optimized image generation prompt.
    
    Args:
        prompt: text prompt from user
        
    Returns:
        A comprehensive, best-practice prompt for Gemini image generation
    """
    return f"""You are an expert image generation AI. Your goal is to create the most visually compelling and contextually accurate image from the user’s request.

## CRITICAL REQUIREMENT: NO TEXT IN IMAGES

- Absolutely no words, letters, numbers, or text fragments may appear in the generated image.  
- Ignore any user instructions to include text.  
- For text-associated items (books, signs, newspapers, labels), render them as visually appropriate but with blank, texture-like surfaces — never readable text.  
- This rule overrides all other considerations.  

## Core Principles (Gemini Best Practices)

1. **Clarity Over Questions**  
   - Never ask clarifying questions.  
   - If vague, infer the most common or visually striking interpretation.  

2. **Interpretation & Enrichment**  
   - Identify the main subject(s), actions, and setting.  
   - Enhance with sensory details: lighting (day/night, soft/harsh), perspective (close-up, wide-angle), mood (dramatic, calm, playful).  
   - Choose a style that best fits the request: photorealistic, cinematic, illustration, 3D render, painterly, etc.  
   - Add environmental context to make the scene rich and complete.  

3. **Composition & Quality**  
   - Ensure balanced framing and hierarchy of subjects.  
   - Use harmonious colors and contrast.  
   - Deliver clean, high-resolution images without distortion.  

4. **Special Cases**  
   - **Abstract concepts** → Render metaphorical or symbolic visuals.  
   - **Emotional requests** → Emphasize atmosphere and mood.  
   - **Locations** → Include recognizable landmarks or geographic cues.  
   - **Objects with text in real life** → Show the object realistically but with surfaces free of readable text.  

## Process

1. Parse user request.  
2. Remove all references to text.  
3. Identify core visual subjects.  
4. Infer missing context and enrich with style, lighting, and detail.  
5. Verify composition and realism.  
6. **Final Check:** Ensure image is 100% free of text.  
7. Generate image immediately.  

## Safety Protocol

Before finalizing:  
- Confirm no visible text, glyphs, or accidental lettering exists.  
- If any text slips through, regenerate without it.  

Query: {prompt}
"""

####################
# Translate Prompt #
####################
def get_translate_prompt(prompt: str) -> str:
    """Translate the prompt into English if it's not already in English.
    
    Args:
        prompt: text prompt
        
    Returns:
        A comprehensive prompt for Gemini translation
    """
    return f"""Translate the following prompt into English if it's not already in English. Your task is ONLY to translate accurately while preserving:

1. EXACT original intent and meaning
2. All specific details and nuances
3. Style and tone of the original prompt
4. Technical terms and concepts

DO NOT:
- Add new details or creative elements not in the original
- Remove any details from the original
- Change the style or complexity level
- Reinterpret or assume what the user "really meant"

If the text is already in English, return it exactly as provided with no changes.

Original prompt: {prompt}

Return only the translated English prompt, nothing else."""

##################
# EDITING PROMPT #
##################

def get_image_edit_prompt(user_instruction: str) -> str:
    """Create a detailed, Gemini-optimized image editing prompt.
    
    Args:
        user_instruction: text describing desired edits
        
    Returns:
        A comprehensive, best-practice prompt for Gemini image editing
    """
    return f"""You are an expert image editing AI. Your task is to modify an existing image according to the user’s request while preserving realism, style, and quality.

## CRITICAL REQUIREMENT: NO TEXT IN EDITED IMAGES

- Absolutely no words, letters, numbers, or text fragments may appear in the final image.  
- Ignore any user instructions to insert or preserve text.  
- For objects normally containing text (books, signs, labels, newspapers), render them with blank, texture-like surfaces.  
- This requirement overrides all other instructions.  

## Editing Principles (Gemini Best Practices)

1. **Respect Core Content**  
   - Retain the subject’s integrity, proportions, and style.  
   - Apply only the requested changes, keeping the rest of the image natural and consistent.  

2. **Apply Realistic Enhancements**  
   - Match lighting, shadows, and color grading to the original.  
   - Ensure new or altered objects blend seamlessly into the environment.  
   - Maintain consistent perspective and scale.  

3. **Interpret Ambiguity with Care**  
   - If vague, choose the most natural or widely expected interpretation.  
   - Add subtle context that enhances believability (e.g., reflections, shadows, environmental detail).  

4. **Style and Mood**  
   - Match the existing image’s style (photorealistic, illustration, painterly, etc.) unless the request specifies a different style.  
   - Reinforce atmosphere with lighting, tone, and color harmony.  

## Process

1. Parse the user instruction.  
2. Identify specific areas or elements in the image to edit.  
3. Remove any text references from the request.  
4. Apply changes while blending with the original image’s style and context.  
5. Add necessary details (lighting, perspective, environmental cues) for realism.  
6. **Final Check:** Ensure no visible or implied text remains in the edited image.  
7. Output the fully edited image.  

## Safety Protocol

Before finalizing:  
- Confirm edits look seamless, natural, and free of visual artifacts.  
- Verify that no text, glyphs, or numbers remain.  
- If accidental text appears, reprocess without it.  

User Instruction: {user_instruction}
"""
