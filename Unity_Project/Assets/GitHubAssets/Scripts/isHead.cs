using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;


public class isHead : MonoBehaviour
{
    private bool isMoving = false;

    public Rigidbody rb;
    public Vector3 rbVelocity;
    public Vector3 rbRotation;
    Quaternion rotation_value;

void Start() {
  rb = GetComponent<Rigidbody>();
  rotation_value=transform.rotation;
    rbRotation=rotation_value.eulerAngles;
    Debug.Log(rbRotation);
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
    rotation_value=transform.rotation;
    rbRotation=rotation_value.eulerAngles;
    Debug.Log(rbRotation);
    
}

public void freezePosition() {
    Debug.Log(rb + " Freezing Positions");
    rb.constraints = RigidbodyConstraints.FreezePosition;
}


}