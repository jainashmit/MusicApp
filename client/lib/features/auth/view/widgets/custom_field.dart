import 'package:flutter/material.dart';

class CustomField extends StatelessWidget {
  final String hint;
  final TextEditingController controller;
  final bool isObscure;
  const CustomField({
    super.key,
    required this.hint,
    required this.controller,
    this.isObscure = false,
  });

  @override
  Widget build(BuildContext context) {
    return TextFormField(
      decoration: InputDecoration(hintText: hint),
      controller: controller,
      obscureText: isObscure,
      validator: (value) {
        if (value!.trim().isEmpty) {
          return "$hint is missing";
        }
        return null;
      },
    );
  }
}
