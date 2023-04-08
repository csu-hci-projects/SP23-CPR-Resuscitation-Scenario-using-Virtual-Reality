using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;


public class isHead : MonoBehaviour
{
    private bool isMoving = false;

    public Rigidbody rb;
    public Vector3 rbVelocity;
    public Vector3 rbRotationX;
    Quaternion rotation_value;

void Start() {
  rb = GetComponent<Rigidbody>();
}

void FixedUpdate ()
{
    rbVelocity = rb.velocity;
    if (isMoving && rbVelocity == Vector3.zero)
    {
        //rb has stopped moving
        isMoving = false;
        freezePosition();
    }
    else if (!isMoving && rbVelocity != Vector3.zero)
    {
        isMoving = true;
    }
    //rotation_value=transform.rotation;
    
    //rbRotationX=rotation_value.eulerAngles.x;
    //Debug.LogWarning(rbRotationX);
    //rbRotation.x = Mathf.Clamp(rbRotation.x, -.5f, .5f);
    //rbRotation.y = Mathf.Clamp(rbRotation.y, -.5f, .5f);
    //rbRotation.z = Mathf.Clamp(rbRotation.z, -.5f, .5f);
    
    //Debug.LogWarning(rotation_value);
}

public void freezePosition() {
    Debug.Log(rb + " Freezing Positions");
    rb.constraints = RigidbodyConstraints.FreezePosition;
}


}